
import os
from pathlib import Path
import itertools

#from modules.nnll_16.src import Backend
#class MetaScrape(Backend)
    # # todo: refine the load methods to work with sharded files
    # from modules.nnll_30.src import read_json_file, write_json_file
    # data = read_json_file("modules/modules.nnll_29/filter.json"")
    # import_map = data["import_map"]
    # method_map = data["method_map"]

from modules.nnll_04.src import load_safetensors_metadata
from modules.nnll_05.src import load_gguf_metadata
from modules.nnll_28.src import load_pickletensor_metadata

def get_model_header(file_path: str) -> tuple:

    safetensors_loader = None
    gguf_loader = None
    pickletensor_loader = None

    #move this and import statements to .json file
    safetensors_extensions = [
        ".safetensors",
        ".sft"
        ]

    gguf_extensions =  [".gguf"]

    pickletensor_extensions = [
        ".pt",
        ".pth",
        ".ckpt",
    ]

    extensions_list = itertools.chain(safetensors_extensions, gguf_extensions, pickletensor_extensions)
    # Get external file metadata
    file_extension = Path(file_path).suffix.lower()
    if file_extension == '' or file_extension is None or file_extension not in list(extensions_list):  # Skip this file if we cannot possibly know what it is
        return
    else:
        if file_extension in safetensors_extensions:
            method_map = load_safetensors_metadata
        elif file_extension in gguf_extensions:
            method_map = load_gguf_metadata
        elif file_extension in pickletensor_extensions:
            method_map = load_pickletensor_metadata

        file_name = os.path.basename(file_path)
        disk_size = os.path.getsize(file_path)

        # Retrieve header by method indicated by extension, usually struct unpacking, except for pt files which are memmap
        model_header = method_map(file_path)
        return (model_header, disk_size, file_name, file_extension)
