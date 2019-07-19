%define debug_package %{nil}

Name:		openjdk
Version:	1.8.0.221
Release:	0
Summary:	OpenJDK 8 Repackaging Official Downloads
License:        Apache-1.1 AND Apache-2.0 AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-with-classpath-exception AND LGPL-2.0-only AND MPL-1.0 AND MPL-1.1 AND SUSE-Public-Domain AND W3C
Group:          Development/Languages/Java
Url:            http://openjdk.java.net/

Source0:	openjdk-%{version}-%{release}.tar.gz

Source1000:	jdk-8u221-linux-arm64-vfp-hflt.tar.gz.00
Source1001:	jdk-8u221-linux-arm64-vfp-hflt.tar.gz.01
Source1100:	jdk-8u221-linux-x64.tar.gz.00
Source1101:	jdk-8u221-linux-x64.tar.gz.01
Source1102:	jdk-8u221-linux-x64.tar.gz.02
Source1103:	jdk-8u221-linux-x64.tar.gz.03

Source2000:	openjdk.manifest

ExclusiveArch:	aarch64 x86_64

Requires:	/bin/basename
Requires:	/bin/cat
Requires:	/bin/cp
Requires:	/bin/gawk
Requires:	/bin/grep
Requires:	/bin/ln
Requires:	/bin/ls
Requires:	/bin/mkdir
Requires:	/bin/mv
Requires:	/bin/pwd
Requires:	/bin/rm
Requires:	/bin/sed
Requires:	/bin/sort
Requires:	/bin/touch
Requires:	/usr/bin/cut
Requires:	/usr/bin/dirname
Requires:	/usr/bin/expr
Requires:	/usr/bin/find
Requires:	/usr/bin/tail
Requires:	/usr/bin/tr
Requires:	/usr/bin/wc
Requires:	/bin/sh

%description
The full openjdk 8 downloaded at
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
This is RPM package of the downloaded tar.gz.

Do NOT install this into deployed images.

%prep

%ifarch aarch64
cat %{SOURCE1000} %{SOURCE1001} > jdk.tar.gz
%endif
%ifarch x86_64
cat %{SOURCE1100} %{SOURCE1101} %{SOURCE1102} %{SOURCE1103} > jdk.tar.gz
%endif

cp %{SOURCE2000} .
mkdir -p install
pushd install
tar -xf jdk.tar.gz
popd

%build

# Nothing to do. They are prebuilt binaries.

%install

mkdir -p %{buildroot}%{_prefix}/java/
pushd install
mv * %{buildroot}%{_prefix}/java/
popd

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/jar jar
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/java java
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/javac javac
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/javah javah
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/javap javap
ln -sf %{_prefix}/java/jdk1.8.0_221/bin/javadoc javadoc
popd

%files
%manifest openjdk.manifest
%defattr(-,root,root,-)
%{_prefix}/java
%{_bindir}/*
