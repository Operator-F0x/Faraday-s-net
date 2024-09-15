from Utils.subnetting import calculate_subnet_from_cidr,calculate_subnet_from_ip_and_mask, show_subnet_details, calculate_subnets
from Utils.ip_utils import ip_to_binary
import os


def main():
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')


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
                4 show binary octet of ip or subnet mask
                0 Exit""")


        function_chosen = input("--> ")

######################################################
        if function_chosen == "1":
            cidr = input("Enter the ip/CIDR -->  ")
            subnet_info = calculate_subnet_from_cidr(cidr)
            print(f"""
    Network Address: {subnet_info['Network Address']}
    Broadcast Address: {subnet_info['Broadcast Address']}
    Usable Hosts Range: {subnet_info['Usable Hosts Range'][0]} to {subnet_info['Usable Hosts Range'][1]}
    """)
        
#end 1
        
######################################################
        if function_chosen == "2":
            ip = input("Enter the IP address --> ")
            subnet_mask = input("Enter the subnet mask --> ")
            
            subnet_info = calculate_subnet_from_ip_and_mask(ip, subnet_mask)
            if subnet_info:
                print(f"""
        Network Address: {subnet_info['Network Address']}
        Broadcast Address: {subnet_info['Broadcast Address']}
        Usable Hosts Range: {subnet_info['Usable Hosts Range'][0]} to {subnet_info['Usable Hosts Range'][1]}
        """)
#end 2

######################################################
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

            print("Want to see the details of a subnet?  - Y or N")
            chose = input("--> ")
            if chose == "Y":
                subnet_number = int(input("Enter the subnet number you want details for --> "))
                if 1 <= subnet_number <= len(subnet_info):
                    show_subnet_details(subnet_info[subnet_number - 1])
                else:
                    print("Invalid subnet number!")
            else:
                return None
#end 3
######################################################            
        if function_chosen == "4":
            ip_or_mask = input("Enter IP address or subnet mask --> ")
            print(f"Binary representation: {ip_to_binary(ip_or_mask)}")
#end 4
        
        if function_chosen == "0":
                break
                
        input("\nPress Enter to continue...")
    #End while              


if __name__ == "__main__":
    main()
