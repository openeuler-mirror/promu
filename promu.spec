%define debug_package %{nil}

Name:    promu
Version: 0.7.0
Release: 2
Summary: Prometheus Utility Tool
License: ASL 2.0
URL:     https://github.com/prometheus/promu

Source0: https://github.com/prometheus/promu/archive/v%{version}.tar.gz

Patch0:  riscv64-support.patch

BuildRequires: golang >= 1.13

Conflicts: promu
Provides:  %{name} = %{version}

%description
promu is the utility tool for building and releasing Prometheus projects

%prep
%setup -q -T -n %{name}-%{version} -b 0
%patch0 -p1 -b .riscv64-support

%build
GOFLAGS=-mod=vendor make build

%install
install -D -m 755 %{name}-%{version} %{buildroot}%{_bindir}/promu

%files
%defattr(-,root,root,-)
%{_bindir}/promu

%changelog
* Wed Jun 29 2022 Jingwiw <wangjingwei@iscas.ac.cn> - 0.7.0-2
- backport to support riscv

* Wed Dec 16 2020 yangzhao <yangzhao1@kylinos.cn> - 0.7.0-1
- Init project promu
