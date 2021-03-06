%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           graphite-api
Summary:        Alternative to Graphite-web
Version:        1.0.2.9999_20150323
Release:        1%{?dist}

License:        Apache 2.0
URL:            http://graphite-api.readthedocs.org
Source0:        https://github.com/brutasse/%{name}/archive/graphite-api-master.zip
Source1:        %{name}.sh
Source2:        %{name}.service
Source3:        %{name}.default
Patch0:         logging_exception.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       pyparsing
Requires:       python-blinker
Requires:       python-cairocffi
Requires:       python-flask
Requires:       python-gunicorn
Requires:       python-jinja2
Requires:       python-six >= 1.8.0
Requires:       python-structlog
Requires:       python-tzlocal
Requires:       pytz
Requires:       PyYAML

%description
Graphite-API is an alternative to Graphite-web, without any built-in dashboard.
Its role is solely to fetch metrics from a time-series database (whisper,
cyanite, etc.) and rendering graphs or JSON data out of these time series. It is
meant to be consumed by any of the numerous Graphite dashboard applications.


%prep
%setup -q -n %{name}-master
# Support for logging exceptions
%patch0 -p2


%build
%{__python} setup.py build


%install
[ "%{buildroot}" != / ] && %{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__mkdir_p} %{buildroot}%{_sysconfdir}/default
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/%{name}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__cp} fpm/conf/etc/%{name}.yaml %{buildroot}%{_sysconfdir}/%{name}.yaml
%{__cp} %{_sourcedir}/%{name}.sh %{buildroot}%{_bindir}/
%{__cp} %{_sourcedir}/%{name}.service %{buildroot}%{_unitdir}/
%{__cp} %{_sourcedir}/%{name}.default %{buildroot}%{_sysconfdir}/default/%{name}
touch %{buildroot}%{_sharedstatedir}/%{name}/index


%clean
[ "%{buildroot}" != / ] && %{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/%{name}.yaml
%config %{_sysconfdir}/default/%{name}
%{python_sitelib}/*
%{_sharedstatedir}/%{name}/index
%{_bindir}/%{name}.sh
%{_unitdir}/%{name}.service


%changelog
* Mon Mar 23 2015 Jiri Tyr <jiri.tyr at gmail.com> 1.0.2.9999-20150323-1
- Removing patch for sumarize function.
- Renaming the source file.

* Fri Jan 9 2015 Jiri Tyr <jiri.tyr at gmail.com> 1.0.2.9999-20150106-2
- Adding patch to fix sumarize function.

* Tue Jan 6 2015 Jiri Tyr <jiri.tyr at gmail.com> 1.0.2.9999-20150106-1
- Adding python-blinker into the dependency list.

* Tue Dec 18 2014 Jiri Tyr <jiri.tyr at gmail.com> 1.0.2.9999-20141218-1
- First build.
