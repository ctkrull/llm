from functions.write_file import write_file

def test_write_file():
    test_wf_1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result for 'lorem.txt': {test_wf_1}")

    test_wf_2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result for 'pkg/morelorem.txt': {test_wf_2}")

    test_wf_3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result for '/tmp/temp.txt': {test_wf_3}")

if __name__ == "__main__":
    test_write_file()