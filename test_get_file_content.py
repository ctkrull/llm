from functions.get_file_content import get_file_content

def test_get_file_content():
    test_gfc = get_file_content("calculator", "lorem.txt")
    print(f"content: {len(test_gfc)}")

    test_gfc_main = get_file_content("calculator", "main.py")
    print(f"Result for 'main.py' file content: \n{test_gfc_main}")

    test_gfc_pkg = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for 'pkg/calculator.py' file content: \n{test_gfc_pkg}")
    
    test_gfc_bin = get_file_content("calculator", "bin/cat")
    print(f"Result for 'bin/cat' file content: \n{test_gfc_bin}")

    test_gfc_nonexist = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for 'pkg/does_not_exist.py' file content: \n{test_gfc_nonexist}")

if __name__ == "__main__":
    test_get_file_content()
