%global scl_version ea-php83
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcached
Version: 3.3.0
Summary: php-memcached extension for %{scl_version}
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcached
Source: v%{version}.tar.gz
Source1: memcached.ini

# should be no requires for building this package
#Requires: memcached
Requires: ea-libmemcached
BuildRequires: cyrus-sasl-devel
BuildRequires: autotools-latest-autoconf
BuildRequires: ea-libmemcached ea-libmemcached-devel
BuildRequires: %{scl_version}
Requires: %{scl_version}-php-common
Requires: %{scl_version}-php-cli

%description
This is the PECL memcached extension, using the libmemcached library to connect
to memcached servers.

%prep
%setup -n php-memcached-%{version}

%build
set -x

scl enable %{scl_version} phpize
scl enable %{scl_version} './configure --with-libmemcached-dir=/opt/cpanel/libmemcached --with-libdir=lib64'
make

%install
set -x

make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcached.so
%config /%{ext_prefix}/%{conf_dir}/memcached.ini

%changelog
* Tue Oct 29 2024 Cory McIntire <cory@cpanel.net> - 3.3.0-1
- EA-12496: Update ea-php83-php-memcached from v3.2.0 to v3.3.0

* Mon Oct 28 2024 Julian Brown <julian.brown@cpanel.net> - 3.2.0-2
- ZC-12246: Correct conffiles for Ubuntu

* Mon Dec 18 2023 Julian Brown <julian.brown@cpanel.net> - 3.2.0-1
- ZC-11488: Build ea-php83-php-memcached

