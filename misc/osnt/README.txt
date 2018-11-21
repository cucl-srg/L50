##################################################################################
# Copyright (c) 2017 Noa Zilberman
# All rights reserved.
#
# This software was developed by the University of Cambridge Computer Laboratory 
# under Leverhulme Trust grant ECF-2016-289 
#
# @NETFPGA_LICENSE_HEADER_START@
#
# Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  NetFPGA licenses this
# file to you under the NetFPGA Hardware-Software License, Version 1.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#   http://www.netfpga-cic.org
#
# Unless required by applicable law or agreed to in writing, Work distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
# @NETFPGA_LICENSE_HEADER_END@
#
################################################################################


Instructions:
1. Clone OSNT-SUME-live
2. Follow the OSNT installation instructions at https://github.com/NetFPGA/OSNT-Public/wiki
3. Program your board with the OSNT bit file, as described in the OSNT wiki
4. Go to the p51 folder
5. make
6. Other supported commands:
	- make clean - clean the folder from unnecessary files
	- make build - copy necessary scripts
	- make traces - generate pcap traces 
	- make oneport - test the latency of a packet sent from (OSNT) port 0 to port 1, without cross traffic
	- make twoport - test the latency of a packet sent from (OSNT) port 0 to port 1, with cross traffic from port 1 to port 0.
	- make allport - test the latency of a packet sent from (OSNT) port 0 to port 1, with cross traffic: port 1 to port 0, port 2 to port 3 and port 3 to port 2
