from functions.get_files_info import get_files_info


def test_get_files_info():
    test_gfi = get_files_info("calculator", ".")
    print(f"Result for current directory: \n{test_gfi}")

    test_gfi_pkg = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory: \n{test_gfi_pkg}")

    test_gfi_bin = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory: \n{test_gfi_bin}")

    test_gfi_outside = get_files_info("calculator", "../")
    print(f"Result for '../' directory: \n{test_gfi_outside}")


if __name__ == "__main__":
    test_get_files_info()