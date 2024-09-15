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
             1 Subnetting for IP + CIDR - (192.168.1.1/24)
             2 Subnetting for IP + Subnet mask - (192.168.1.1 255.255.255.0)
             3 Calculate subnets from IP and desired number of subnets - (192.168.1.1 5)
             4 Show binary octet of IP or subnet mask""")
    
    function_chosen = input("--> ")
    if function_chosen == "1":
        cidr = input("Enter the IP/CIDR -->  ")
        subnet_info = calculate_subnet_from_cidr(cidr)
        print(f"""
Network Address: {subnet_info['Network Address']}
Broadcast Address: {subnet_info['Broadcast Address']}
Usable Hosts Range: {subnet_info['Usable Hosts Range'][0]} to {subnet_info['Usable Hosts Range'][1]}
""")


    if function_chosen == "3":
        ip = input("Enter IP -->  ")
        num_subnet = int(input("Enter the number of subnets you want -->"))

        subnet_info = calculate_subnets(ip, num_subnet)
        
        for info in subnet_info:
                print(f"Subnet {info['Subnet']}:")
                print(f"  Network Address: {info['Network Address']}")
                print(f"  Subnet Mask: {info['Subnet Mask']}")
                print(f"  Broadcast Address: {info['Broadcast Address']}")
                print(f"  Gateway (first host): {info['Gateway (primo host)']}")
                print(f"  Last Usable Host: {info['Last Usable Host']}")
                print(f"  Total Usable Hosts: {info['Total Usable Hosts']}")
                print()

        print("Want to see the details of a subnet?  - Y or N")
        choice = input("--> ")
        if choice == "Y":
            subnet_number = int(input("Enter the subnet number you want details for --> "))
            if 1 <= subnet_number <= len(subnet_info):
                show_subnet_details(subnet_info[subnet_number - 1])
            else:
                print("Invalid subnet number!")
        else:
            return None            


if __name__ == "__main__":
    main()
