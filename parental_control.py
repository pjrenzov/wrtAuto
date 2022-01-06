def ParentalConroll(ipaddr,name,startTime,endTime):
    commandtxt = ['uci add firewall rule',
'uci set firewall.@rule[-1].name="{}"'.format(name),
'uci set firewall.@rule[-1].src="lan"',
'uci set firewall.@rule[-1].src_ip="{}"'.format(ipaddr),
'uci set firewall.@rule[-1].dest="wan"',
'uci set firewall.@rule[-1].start_time="{}"'.format(startTime),
'uci set firewall.@rule[-1].stop_time="{}"'.format(endTime),
'uci set firewall.@rule[-1].target="REJECT"',
'uci commit firewall',
'/etc/init.d/firewall restart'
    ]
    return  commandtxt