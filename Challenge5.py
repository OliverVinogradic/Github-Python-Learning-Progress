error_list = [404, 500, 999, 404, 403, 502]

error_mapping = {
    404: "Not Found",
    500: "Internal Server Error",
    403: "Forbidden",
    502: "Bad Gateway"
}

def translateErrors(errors, mapping):
     result_list = []
     for code in errors:
          text = mapping.get(code,"Unknown Error")
          result_list.append(text)
     
     return result_list

def main():
     result = translateErrors(error_list,error_mapping)         
     print(result) 



if __name__ == "__main__":
     main()