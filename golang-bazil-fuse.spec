# Run tests in check section
# Deactivating test: tests depends on fuse being present and fuse.ko being 
# loaded but the chroot doesn't allow to insert module.
%bcond_with check

%global goipath         bazil.org/fuse
%global forgeurl        https://github.com/bazil/fuse
%global commit          65cc252bf6691cb3c7014bcb2c8dc29de91e3a7e

%global common_description %{expand:
Go library for writing FUSE userspace filesystems.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.8%{?dist}
Summary: Go library for writing FUSE userspace filesystems
License: BSD and MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/sys/unix)

%description
%{common_description}


%package    devel
Summary:    %{summary}
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md doc examples


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20180628git65cc252
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20180628git65cc252
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git65cc252
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180628git65cc252
- Bump to commit 65cc252bf6691cb3c7014bcb2c8dc29de91e3a7e

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180313git371fbbd
- Fix BuildRequires 

* Wed Mar 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180313git371fbbd
- Update with the new Go packaging
- Add doc and examples
- Make devel package arched

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160811git371fbbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20160811git371fbbd
- First package for Fedora


