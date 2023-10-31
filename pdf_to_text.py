from tika import parser
import os, argparse

# function for text convertion 
def convert_pdf_to_text(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path_to_pdf = os.path.join(root, file)
            [stem, ext] = os.path.splitext(path_to_pdf)
            if ext == '.pdf':
                print("Processing " + path_to_pdf)
                pdf_contents = parser.from_file(path_to_pdf,service='text')
                path_to_txt = stem + '.txt'
                with open(path_to_txt, 'w',encoding='utf-8') as txt_file:
                    print("Writing contents to " + path_to_txt)
                    txt_file.write(pdf_contents['content'])

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--dir_path", type=str, default=".", help="Input pdfs directory path")
    args = arg_parser.parse_args()
    convert_pdf_to_text(args.dir_path)