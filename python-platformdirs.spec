%define		module	platformdirs
Summary:	Python module for determining appropriate platform-specific dirs
Name:		python-%{module}
Version:	2.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/platformdirs/
Source0:	https://files.pythonhosted.org/packages/source/p/platformdirs/%{module}-%{version}.tar.gz
# Source0-md5:	e11ea2bee61b06c46e7db5576cc56624
URL:		https://pypi.org/project/platformdirs/
BuildRequires:	python-modules >= 2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
