import zlib,base64

def compressor(input_file,output_file):
    try:
        with open(input_file) as file:
            uncomp_data=file.read()
        #print(uncomp_data)
        byte_data=bytes(uncomp_data,'utf-8')
        #print(byte_data)
        comp_data=zlib.compress(byte_data,9)
        #print(comp_data)
        encode_data=base64.b64encode(comp_data)#produces output as bytes,comp_dta
        #print(encod_data)
        decode_data=encode_data.decode('utf-8')
        with open(output_file,'w') as file:
            file.write(decode_data)
        return "compressed successfully!! ;))"
    except Exception as e:
        return f"compression failed {str(e)}"
    

def decompressor(input_file,final_file):
    try:
        with open(input_file,'rb') as file:
            encode_data=file.read()
        decode_data=base64.b64decode(encode_data)
        ori_data=zlib.decompress(decode_data)
        with open(final_file,'wb') as file:
            file.write(ori_data)
        return "compressed successfully!! ;))"
    except Exception as e:
        return f"decompression failed {str(e)}"

# if __name__ == "__main__":
#     compressor("old.txt","new.txt")
#     decompressor("new.txt","new2.txt")
#     print("compression achieved!!")

