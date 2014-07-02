%global sname oslo.vmware

Name:           python-oslo-vmware
Version:        0.3
Release:        1%{?dist}
Summary:        Oslo VMware library for OpenStack projects

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{sname}/%{sname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-stevedore
BuildRequires:  python-netaddr
BuildRequires:  python-iso8601
BuildRequires:  python-six
BuildRequires:  python-babel
BuildRequires:  python-suds
BuildRequires:  python-eventlet
BuildRequires:  PyYAML

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package doc
Summary:    Documentation for OpenStack common VMware library
Group:      Documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description doc
Documentation for OpenStack common VMware library.

%prep

%setup -q -n %{sname}-%{version}

# Remove bundled egg-info
rm -rf %{sname}.egg-info

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/
%{python2_sitelib}/%{sname}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{sname}-%{version}-py?.?.egg-info

%files doc
%doc html doc/source/readme.rst

%changelog
* Wed Jun 25 2014 Jon Bernard <jobernar@redhat.com> - 0.3-1
- Initial package from Alan Pevec <apevec@redhat.com>
  with cleanups by Jon Bernard