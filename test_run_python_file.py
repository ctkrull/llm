from functions.run_python_file import run_python_file

def test_run_python_file():
    test_rpf_mp = run_python_file("calculator", "main.py")
    print(f"{test_rpf_mp}")

    test_rpf_mpc = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"{test_rpf_mpc}")

    test_rpf_test = run_python_file("calculator", "tests.py")
    print(f"{test_rpf_test}")

    test_rpf_outside = run_python_file("calculator", "../main.py")
    print(f"{test_rpf_outside}")

    test_rpf_exist = run_python_file("calculator", "nonexistent.py")
    print(f"{test_rpf_exist}")

    test_rpf_lt = run_python_file("calculator", "lorem.txt")
    print(f"{test_rpf_lt}")

if __name__ == "__main__":
    test_run_python_file()
