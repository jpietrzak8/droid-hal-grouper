%define device grouper
%define vendor asus

%define vendor_pretty Asus
%define device_pretty Nexus 7 (2012)

%define installable_zip 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
