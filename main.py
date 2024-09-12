from Subnetting.SubneTools import calculate_subnet_from_cidr
from Subnetting.SubneTools import calculate_subnets
from Subnetting.SubneTools import display_subnet_info
from Subnetting.SubneTools import show_subnet_details

def main():
    print("""                                                                                                                       
                   *                         +                   
                   @                         @                   
                  @@@                       @@@                  
                  @ @@                    .@@ @                  
                 @:  @@                  :@@  @-                 
                 @  @ =@@               @@  @ @@                 
                 @  @@  @@.           -@@  %@ @@                 
                 @: @@@. @@          @@   *@% @*                 
                 %@ @@@@   @=       @@  +**@  @                  
                  @  @@@@    @@@@@+     ***@ +@                  
                  @@ @@@@+             @@*@. @#                  
                   @- @@                =@@ @@                   
                   .-                       *                    
                   -@                       @                    
                   @                         @                   
                 @.   .@.                @      @                 
                 @@@@@%                     @@@@@                      
                %@@@@@@                    @@@@@@*.                                                                  
                   @#-.                  @@@#.                   
                         #@          @@=                         
                           @@       @@                           
                            .@     @                             
                              @@@@@""")
    
    print("""
             1 Subnetting for ip + CIDR - (192.168.1.1/24)
             2 Subnetting for ip + Subnet mask - (192.168.1.1 255.255.255.0)
             3 calculate subnets from ip and desired subnets number - (192.168.1.1 5)
             4 show binary octet of ip or subnet mask""")
    
    function_chosen = input("--> ")
    if function_chosen == "1":
        cidr = input("Enter the ip/CIDR -->  ")
        subnet_info = calculate_subnet_from_cidr(cidr)
        print(f"Network Address: {subnet_info['Network Address']}")
        print(f"Broadcast Address: {subnet_info['Broadcast Address']}")
        print(f"Usable Hosts Range: {subnet_info['Usable Hosts Range'][0]} to {subnet_info['Usable Hosts Range'][1]}")

    if function_chosen == "3":
        ip = input("Enter ip -->  ")
        num_subnet = int(input("Enter number of subnet you want -->"))

        subnet_info = calculate_subnets(ip, num_subnet)
        
        for info in subnet_info:
                print(f"Subnet {info['Subnet']}:")
                print(f"  Network Address: {info['Network Address']}")
                print(f"  Subnet Mask: {info['Subnet Mask']}")
                print(f"  Broadcast Address: {info['Broadcast Address']}")
                print(f"  Gateway (primo host): {info['Gateway (primo host)']}")
                print(f"  Last Usable Host: {info['Last Usable Host']}")
                print(f"  Total Usable Hosts: {info['Total Usable Hosts']}")
                print()

        subnet_number = int(input("Enter the subnet number you want details for --> "))
        if 1 <= subnet_number <= len(subnet_info):
            show_subnet_details(subnet_info[subnet_number - 1])
        else:
            print("Invalid subnet number!")

if __name__ == "__main__":
    main()
