#!/usr/bin/env python3
import os
import sys
import json
import re
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def active_design_points(project_dir):
    """Finds active design points in project folder."""
    dp_values = []

    # Regular expression to match folder names like dp0, dp1, dp20, etc.
    pattern = re.compile(r"dp(\d+)")

    # Loop through items in the directory
    for item in os.listdir(project_dir):
        match = pattern.fullmatch(item)
        if match:
            dp_values.append(int(match.group(1)))  # Convert to int for sorting
    return dp_values


def load_parameters(param_file):
    """Load parameters from a JSON file."""
    with open(param_file, 'r') as f:
        return json.load(f)


def render_template(template_dir, template_file, parameters):
    """Render the Jinja2 template with the provided parameters."""
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)
    return template.render(parameters)


def generate_files(extension_name, bg_directory, bg_name, design_points, project_dir, template_dir, template_file, params_file):
    """Generates the files for each of the design point folders."""

    dp_dir = []
    for i in range(len(design_points)):

        dp_dir.append(Path(project_dir).joinpath(f"dp{i}"))

        params_path = Path(dp_dir[i]).joinpath(f"{extension_name}\\ACT\\{params_file}")

        if 1 - params_path.exists():
            params_path = os.path.join(template_dir, params_file)

        # Load the parameters
        parameters = load_parameters(params_path)

        output_dir = Path(dp_dir[i]).joinpath(f"{bg_directory}\\TS")  # Directory to save the generated file
        output_file = bg_name

        [f.unlink() for f in Path(output_dir).glob("*") if f.is_file()]  # Deletes files in output_dir

        # Render the template with the parameters
        rendered_content = render_template(template_dir, template_file, parameters)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Write the rendered content to a new file
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, 'w') as f:
            f.write(rendered_content)


def main():

    params_file = 'params.json'  # JSON file containing parameter values

    default_params = load_parameters(params_file)

    project_dir = default_params["Project_Directory"]
    template_dir = default_params["Template_Directory"]
    template_file = default_params["Template_Name"]
    extension_name = default_params["Extension_Name"]
    bg_directory = default_params["BG_Directory"]
    bg_name = default_params["BG_Name"]

    design_points = active_design_points(project_dir)

    generate_files(extension_name, bg_directory, bg_name, design_points, project_dir, template_dir, template_file, params_file)


main()

if __name__ == "__main__":
    main()
