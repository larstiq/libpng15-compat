# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.24
# 

Name:       libpng15-compat

# >> macros
%define _unpackaged_files_terminate_build 0
# << macros

Summary:    A library of functions for manipulating PNG image format files
Version:    1.5.21
Release:    1
Group:      System/Libraries
License:    zlib
URL:        http://www.libpng.org/pub/png/libpng.html
Source0:    ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.xz
Source100:  libpng15-compat.yaml
Patch0:     libpng-multilib.patch
Patch1:     libpng-%{version}-apng.patch.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)

%description
The libpng15-compat package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng15-compat should be installed if you need to manipulate PNG format image
files.

%prep
%setup -q -n libpng-%{version}

# libpng-multilib.patch
%patch0 -p1
# libpng-%{version}-apng.patch.gz
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
%ifarch %{arm}
    --enable-arm-neon
%endif

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc LICENSE
%{_libdir}/libpng*.so.*
# << files
