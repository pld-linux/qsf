Summary:	Quick spam filter
Name:		qsf
Version:	0.9.9
Release:	0.1
License:	Artistic
Group:		Applications
Source0:	http://dl.sourceforge.net/qsf/%{name}-%{version}.tar.gz
# Source0-md5:	dfd9e79f049c1e9832f8d70e2c84fe7e
URL:		http://www.ivarch.com/programs/qsf.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quick Spam Filter (qsf) is a small, fast spam filter that works by
learning to recognise the words that are more likely to appear in spam
than non-spam. It is intended to be used in a procmail recipe to mark
email as being possible spam.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/COPYING doc/NEWS doc/TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
