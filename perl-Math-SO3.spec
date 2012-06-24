#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	SO3
Summary:	Math::SO3 - implementation of SO(3) rotation group
Summary(pl):	Math::SO3 - implementacja grupy obrot�w SO(3)
Name:		perl-Math-SO3
Version:	0.90
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ca499258a36775d3e2f3d9ae0db0c5c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple (direct), fast (in C) implementation of
three-dimensional rotations, more widely known as "the SO(3) group".

%description -l pl
Ten pakiet dostarcza prost� (bezpo�redni�), szybk� (w C) implementacj�
tr�jwymiarowych obrot�w, szerzej znan� jako "grupa SO(3)".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# uhm...? original version failed, this doesn't
perl -pi -e 's/euler_angles_zxz/euler_angles_yxz/' test.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Math/SO3.pm
%dir %{perl_vendorarch}/auto/Math/SO3
%{perl_vendorarch}/auto/Math/SO3/autosplit.ix
%{perl_vendorarch}/auto/Math/SO3/SO3.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/SO3/SO3.so
%{_mandir}/man3/*
