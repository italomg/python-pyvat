%global sname pyvat
%global owner iconfinder

Name:       python-%{sname}
Version:    1.3.15
Release:    1%{?dist}
Summary:    VAT validation and calculation for Python
License:    ASL 2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/refs/tags/v%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}
BuildArch:  noarch

BuildRequires:  python3-devel
Requires:       python3

%description
With EU VAT handling rules becoming ever more ridiculous and complicated,
businesses within the EU are faced with the complexity of having to
validate VAT numbers. pyvat was built for
Iconfinder's marketplace to handle just this problem.

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
With EU VAT handling rules becoming ever more ridiculous and complicated,
businesses within the EU are faced with the complexity of having to
validate VAT numbers. pyvat was built for
Iconfinder's marketplace to handle just this problem.

%prep
%autosetup -p1 -n %{sname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

# check
# These tests require unittest2 to run as the project is compatible with Ptyhon 2 versions
# unittest2 was intentially removed from Fedora repositories see https://bugzilla.redhat.com/show_bug.cgi?id=1794222

%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Jul 19 2022 Italo Garcia <italo.garcia@aiven.io> - 1.3.15-1
- Initial package
