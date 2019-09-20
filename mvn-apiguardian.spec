#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-apiguardian
Version  : 1.0.0
Release  : 1
URL      : https://github.com/apiguardian-team/apiguardian/archive/r1.0.0.tar.gz
Source0  : https://github.com/apiguardian-team/apiguardian/archive/r1.0.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.jar
Source2  : https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-apiguardian-data = %{version}-%{release}
Requires: mvn-apiguardian-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
# @API Guardian
## Continuous Integration Builds
| CI Server | OS      | Status | Description |
| --------- | ------- | ------ | ----------- |
| Jenkins   | Linux   | [![Build Status](https://junit.ci.cloudbees.com/buildStatus/icon?job=API_Guardian)](https://junit.ci.cloudbees.com/job/API_Guardian) | Official CI build server for @API Guardian |
| Travis CI | Linux   | [![Travis CI build status](https://travis-ci.org/apiguardian-team/apiguardian.svg?branch=master)](https://travis-ci.org/apiguardian-team/apiguardian) | Used to perform quick checks on submitted pull requests |

%package data
Summary: data components for the mvn-apiguardian package.
Group: Data

%description data
data components for the mvn-apiguardian package.


%package license
Summary: license components for the mvn-apiguardian package.
Group: Default

%description license
license components for the mvn-apiguardian package.


%prep
%setup -q -n apiguardian-r1.0.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-apiguardian
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-apiguardian/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.jar
/usr/share/java/.m2/repository/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-apiguardian/LICENSE
