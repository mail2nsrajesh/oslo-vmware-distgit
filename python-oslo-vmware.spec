%global sname oslo.vmware

Name:           python-oslo-vmware
Version:        0.3
Release:        3%{?dist}
Summary:        Oslo VMware library for OpenStack projects

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{sname}/%{sname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr

Requires:  python-stevedore
Requires:  python-netaddr
Requires:  python-iso8601
Requires:  python-six
Requires:  python-babel
Requires:  python-suds
Requires:  python-eventlet
Requires:  PyYAML

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

%setup -q -n %{sname}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{sname}.egg-info

%build
%{__python2} setup.py build

# generate html docs
python setup.py build_sphinx

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/%{sname}-%{version}*.pth
%{python2_sitelib}/%{sname}-%{version}*.egg-info

%files doc
%doc doc/build/html doc/source/readme.rst

%changelog
* Tue Sep 16 2014 Derek Higgins <derekh@redhat.com> - XXX
- Generate docs with setup.py (as upsteam have)
- remove extra entrees from %files

* Fri Aug 1 2014 Jon Bernard <jobernar@redhat.com> - 0.3-3
- Fix mistake in runtime requirements
* Wed Jul 2 2014 Jon Bernard <jobernar@redhat.com> - 0.3-2
- Update spec file to build successfully on el6
* Wed Jun 25 2014 Jon Bernard <jobernar@redhat.com> - 0.3-1
- Initial package from Alan Pevec <apevec@redhat.com>
  with cleanups by Jon Bernard
