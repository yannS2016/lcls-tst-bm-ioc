#IOC_TOP = /cds/group/pcds/epics/ioc/common/ads-ioc/R0.8.0
IOC_TOP = /cds/home/z/zlentz/github/ioc-common-ads-ioc
IOC_INSTANCE_PATH := $(shell pwd)

# Set PRODUCTION_IOC to 1 to move from a testing to a production IOC:
PRODUCTION_IOC := 0

PROJECT_NAME = lcls-plc-tst-ioc
PROJECT_PATH := ../../TestIOC/TestIOC.tsproj
PLC = TestIOC

PYTMC_OPTS :=
PREFIX = PLC:TST:IOC

include $(IOC_TOP)/iocBoot/templates/Makefile.base
