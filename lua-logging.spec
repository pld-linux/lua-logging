# TODO
# - noarch pkg?
Summary:	LuaLogging provides a simple API to use logging features in Lua
Summary(hu.UTF-8):	LuaLogging egy egyszerű API-t biztosít naplózó funkciókhoz Lua-ban.
Name:		lua-logging
Version:	1.1.4
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/2693/lualogging-%{version}.tar.gz
# Source0-md5:	72a8622748a525f5fb8ed23278326f80
URL:		http://www.keplerproject.org/lualogging/
BuildRequires:	lua51-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaLogging provides a simple API to use logging features in Lua.

%description -l hu.UTF-8
LuaLogging egy egyszerű API-t biztosít naplózó funkciókhoz Lua-ban.

%prep
%setup -q -n lualogging-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.1
%{__make} install \
    PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
# XXX parent dir deps from where?
%dir %{_datadir}/lua/5.1/logging
%{_datadir}/lua/5.1/logging/*.lua
%{_datadir}/lua/5.1/logging.lua
