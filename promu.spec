%define debug_package %{nil}

Name:    promu
Version: 0.7.0
Release: 1
Summary: Prometheus Utility Tool
License: ASL 2.0
URL:     https://github.com/prometheus/promu

Source0: https://github.com/prometheus/promu/archive/v%{version}.tar.gz

BuildRequires: golang >= 1.13

Conflicts: promu
Provides:  %{name} = %{version}

%description
promu is the utility tool for building and releasing Prometheus projects

%prep
%setup -q -T -n %{name}-%{version} -b 0

%build
GOFLAGS=-mod=vendor make build

%install
install -D -m 755 %{name}-%{version} %{buildroot}%{_bindir}/promu

%files
%defattr(-,root,root,-)
%{_bindir}/promu

%changelog
* Tue Dec 16 2020 yangzhao <yangzhao1@kylinos.cn> - 0.7.0-1
- Init project promu
