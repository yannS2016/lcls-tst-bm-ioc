#IOC_TOP = /cds/group/pcds/epics/ioc/common/ads-ioc/R1.0.2
IOC_TOP = /cds/group/pcds/epics-dev/nlentz/ads-ioc-dev-directory/ioc-common-ads-ioc
IOC_INSTANCE_PATH := $(shell pwd)

# Set PRODUCTION_IOC to 1 to move from a testing to a production IOC:
PRODUCTION_IOC := 0

PROJECT_NAME = lcls-plc-tst-ioc
PROJECT_PATH := ../../TestIOC/TestIOC.tsproj
PLC = TestIOC

PYTMC_OPTS :=
PREFIX = PLC:TST:IOC

include $(IOC_TOP)/iocBoot/templates/Makefile.base
