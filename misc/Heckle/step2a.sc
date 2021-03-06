#!/bin/bash +x

#Script to copy heckle-specific files to bblogin

#copy source code to site packages and dist packages

COBALT_PATH=$HOME/cobalt/trunk

COBALT_COMP_PATH=$COBALT_PATH/src/lib/Components
COBALT_REFERENCE_PATH=$COBALT_PATH/src/components

COBALT_MISC_PATH=$COBALT_PATH/misc/Heckle

SYSTEM_LIB_PATH=/usr/lib/python2.6/site-packages/Cobalt
SYSTEM_COMP_PATH=$SYSTEM_LIB_PATH/Components
SYSTEM_DATATYPES_PATH=$SYSTEM_LIB_PATH/DataTypes

SYSTEM_BIN_PATH=/usr/local/bin

cd ~/cobalt/trunk
svn update
cd ~

for component in heckle_system.py heckle_system2.py heckle_processgroup.py heckle_lib.py heckle_resource.py; do
     sudo cp $COBALT_COMP_PATH/$component $SYSTEM_COMP_PATH/$component
     echo "Did $component"
done

for component in heckle_system.py heckle_system2.py; do
     sudo cp $COBALT_REFERENCE_PATH/$component $SYSTEM_BIN_PATH/$component
     sudo chmod +x $SYSTEM_BIN_PATH/$component
     echo "Did reference $component"
done

sudo cp $COBALT_MISC_PATH/heckle_forker.py $SYSTEM_COMP_PATH/heckle_forker.py
echo "Did heckle_forker.py"
sudo cp $COBALT_MISC_PATH/heckle_sched.py $SYSTEM_COMP_PATH/heckle_sched.py
echo "Did heckle_sched.py"
sudo cp $COBALT_MISC_PATH/heckle_temp_Data.py $SYSTEM_LIB_PATH/heckle_temp_Data.py
echo "Did heckle_temp_Data.py"
sudo cp $COBALT_MISC_PATH/heckle_temp_ProcessGroup.py $SYSTEM_DATATYPES_PATH/heckle_temp_ProcessGroup.py
echo "Did heckle_temp_ProcessGroup.py"



sudo cp $COBALT_MISC_PATH/heckle_forker_reference.py $SYSTEM_BIN_PATH/heckle_forker.py
sudo chmod +x $SYSTEM_BIN_PATH/heckle_forker.py
echo "Did reference heckle_forker.py"

sudo cp $COBALT_MISC_PATH/heckle_sched_reference.py $SYSTEM_BIN_PATH/heckle_sched.py
sudo chmod +x $SYSTEM_BIN_PATH/heckle_sched.py
echo "Did reference heckle_sched.py"


for component in copy update commit step2a.sc; do
     cp $COBALT_MISC_PATH/$component $HOME/$component
done