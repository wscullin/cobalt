#!/usr/bin/python

import time, sys
#from FTBEventAction import *
from ftb import *

ftb = FTB()

ftb.FTB_Connect("0.5", "FTB.APP01.ES01", "app02", "0", "FTB_SUBSCRIPTION_NONE", 0)
ftb.FTB_Declare_publishable_events( None, [ ["ETYPE02", "INFO"] ], 1);

# shandle=ftb.FTB_subscribe_handle_t()
# ftb.FTB_Subscribe( shandle,"event_name=E01", None, None)

while True:
	ehandle = ftb.FTB_event_handle_t()
	ftb.FTB_Publish("ETYPE02",ehandle);
	print 'Published: ETYPE02' 
	time.sleep(2)
# 	ehandle = ftb.FTB_event_handle_t()
# 	ftb.FTB_Publish("E02",ehandle);
# 	print 'Published: E02' 
# 	time.sleep(2)

