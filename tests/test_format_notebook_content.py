import json
import pathlib

import blackbook


def test_format_notebook_content():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    print(f"data_path: {data_path}\n")
    source_notebook_path = data_path / "unformatted" / "spaces.ipynb"
    print(f"source_notebook_path: {source_notebook_path}\n")
    output_json = blackbook.format_notebook_content(source_notebook_path)
    print(f"output_json: {output_json}\n")

    formatted_notebook_path = data_path / "formatted" / "spaces.ipynb"
    # print(f"formatted_notebook_path: {formatted_notebook_path}\n")
    expected_content = formatted_notebook_path.read_text()
    # print(f"expected_content: {expected_content}\n")
    expected_json = json.loads(expected_content)
    # print(f"expected_json: {expected_json}\n")
    print(
        [
            cell["source"] == expected_cell["source"]
            for cell, expected_cell in zip(output_json["cells"], expected_json["cells"])
        ]
    )
    print(
        all(
            [
                cell["source"] == expected_cell["source"]
                for cell, expected_cell in zip(
                    output_json["cells"], expected_json["cells"]
                )
            ]
        )
    )
    assert all(
        [
            cell["source"] == expected_cell["source"]
            for cell, expected_cell in zip(output_json["cells"], expected_json["cells"])
        ]
    )


def test_format_notebook_content_does_nothing_with_formatted_notebook():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    formatted_notebook_path = data_path / "formatted" / "spaces.ipynb"
    assert blackbook.format_notebook_content(formatted_notebook_path) is None
