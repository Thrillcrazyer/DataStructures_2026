from pathlib import Path
import shutil
import subprocess

import torch


def format_tensor_value(tensor):
	if tensor.numel() == 1:
		return f"{tensor.item():.4f}"
	return f"shape={tuple(tensor.shape)}"


def build_autograd_dot(output_tensor, params=None):
	params = params or {}
	tensor_names = {id(tensor): name for name, tensor in params.items()}
	nodes = []
	edges = []
	function_node_ids = {}
	seen_tensors = set()

	def add_tensor_node(tensor, name=None):
		tensor_id = f"tensor_{id(tensor)}"
		if tensor_id in seen_tensors:
			return tensor_id

		seen_tensors.add(tensor_id)
		title = name or tensor_names.get(id(tensor), "tensor")
		label = (
			f"{{{title}|data={format_tensor_value(tensor)}"
			f"|requires_grad={tensor.requires_grad}}}"
		)
		nodes.append(
			f'  "{tensor_id}" [shape=record, style="rounded,filled", '
			f'fillcolor="#FFF2CC", label="{label}"];'
		)
		return tensor_id

	def add_function_node(fn):
		if fn in function_node_ids:
			return function_node_ids[fn]

		fn_id = f"fn_{len(function_node_ids)}"
		function_node_ids[fn] = fn_id

		nodes.append(
			f'  "{fn_id}" [shape=box, style="filled", '
			f'fillcolor="#D9EAF7", label="{type(fn).__name__}"];'
		)

		if hasattr(fn, "variable"):
			variable = fn.variable
			variable_id = add_tensor_node(variable, tensor_names.get(id(variable), "leaf"))
			edges.append(f'  "{variable_id}" -> "{fn_id}";')

		for parent_fn, _ in fn.next_functions:
			if parent_fn is None:
				continue
			parent_id = add_function_node(parent_fn)
			edges.append(f'  "{parent_id}" -> "{fn_id}";')

		return fn_id

	output_id = add_tensor_node(output_tensor, tensor_names.get(id(output_tensor), "output"))
	if output_tensor.grad_fn is not None:
		fn_id = add_function_node(output_tensor.grad_fn)
		edges.append(f'  "{fn_id}" -> "{output_id}";')

	dot_lines = [
		"digraph AutogradGraph {",
		"  rankdir=LR;",
		'  graph [bgcolor="white"];',
		'  node [fontname="Helvetica"];',
		'  edge [fontname="Helvetica"];',
		*nodes,
		*edges,
		"}",
	]
	return "\n".join(dot_lines)


def save_graph(dot_source, output_dir, stem="backward_graph"):
	dot_path = output_dir / f"{stem}.dot"
	dot_path.write_text(dot_source, encoding="utf-8")
	print(f"DOT saved to: {dot_path}")

	if shutil.which("dot") is None:
		print("Graphviz 'dot' command not found. Install Graphviz to render PNG.")
		return

	png_path = output_dir / f"{stem}.png"
	subprocess.run(["dot", "-Tpng", str(dot_path), "-o", str(png_path)], check=True)
	print(f"PNG saved to: {png_path}")


if __name__ == "__main__":
	x = torch.tensor(2.0, requires_grad=True)
	y = torch.tensor(3.0, requires_grad=True)
	z = torch.tensor(4.0, requires_grad=True)
	f = x * y + torch.exp(y + x.pow(2) + z)
	f.backward()

	print(f"f = {f.item():.4f}")
	print(f"df/dx = {x.grad.item():.4f}")
	print(f"df/dy = {y.grad.item():.4f}")
	print(f"df/dz = {z.grad.item():.4f}")

	dot_source = build_autograd_dot(f, params={"x": x, "y": y, "z": z, "f": f})
	save_graph(dot_source, Path(__file__).parent)
