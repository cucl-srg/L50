cd /root/MoonGen
sudo ./bind-interfaces.sh
sudo ./setup-hugetlbfs.sh

# Line below for testing MoonGen. Connect two ports of NIC together.
# sudo ./build/MoonGen examples/l3-load-latency.lua 0 1
