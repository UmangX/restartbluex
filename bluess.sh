echo "
██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗░██████╗░██╗░░██╗
██║░░░██║████╗░████║██╔══██╗████╗░██║██╔════╝░╚██╗██╔╝
██║░░░██║██╔████╔██║███████║██╔██╗██║██║░░██╗░░╚███╔╝░
██║░░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░╚██╗░██╔██╗░
╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║╚██████╔╝██╔╝╚██╗
░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝"

echo "Running The Reset" 
echo "List of the devices that were paired"

echo "------------------------------------"
bluetoothctl devices 
echo "------------------------------------"
bluetoothctl disconnect  04:3E:2B:D8:A3:F5
echo "------------------------------------"
sleep 2
bluetoothctl connect 04:3E:2B:D8:A3:F5
echo "------------------------------------"
exit 
