#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : compat-openssl-soname-110
Version  : 1.1.0l
Release  : 102
URL      : https://www.openssl.org/source/old/1.1.0/openssl-1.1.0l.tar.gz
Source0  : https://www.openssl.org/source/old/1.1.0/openssl-1.1.0l.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : GPL-2.0
Requires: compat-openssl-soname-110-lib = %{version}-%{release}
Requires: ca-certs
Requires: ca-certs-static
Requires: p11-kit
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : autogen
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-cpan
BuildRequires : buildreq-qmake
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : dbus-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : file-dev
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : libcap-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libstdc++
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : linux-dev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : m4
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : p11-kit
BuildRequires : perl(Test::More)
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : popt-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : unzip
BuildRequires : util-linux-bin
BuildRequires : util-linux-extras
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zip
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-clearlinux-CFLAGS-during-build.patch
Patch2: 0002-Hide-a-symbol-from-Steam.patch
Patch3: 0003-Use-OS-provided-copy-of-openssl.cnf-as-fallback.patch

%description
OpenSSL 1.1.0l 10 Sep 2019
All rights reserved.
DESCRIPTION
-----------
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Transport Layer Security (TLS) protocols (including SSLv3) as well as a
full-strength general purpose cryptographic library.

%package lib
Summary: lib components for the compat-openssl-soname-110 package.
Group: Libraries

%description lib
lib components for the compat-openssl-soname-110 package.


%package lib32
Summary: lib32 components for the compat-openssl-soname-110 package.
Group: Default

%description lib32
lib32 components for the compat-openssl-soname-110 package.


%package staticdev
Summary: staticdev components for the compat-openssl-soname-110 package.
Group: Default

%description staticdev
staticdev components for the compat-openssl-soname-110 package.


%package staticdev32
Summary: staticdev32 components for the compat-openssl-soname-110 package.
Group: Default

%description staticdev32
staticdev32 components for the compat-openssl-soname-110 package.


%prep
%setup -q -n openssl-1.1.0l
cd %{_builddir}/openssl-1.1.0l
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a openssl-1.1.0l build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620030466
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
./config zlib shared --prefix=/usr --openssldir=/etc/ssl --libdir=lib64
## make_prepend content
make depend LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a -Wl,--no-whole-archive -Wl,--no-whole-archive"
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a -Wl,--no-whole-archive -Wl,--no-whole-archive"

LD_PRELOAD="./libcrypto.so ./libssl.so" apps/openssl speed rsa
make -j16 test V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a -Wl,--no-whole-archive -Wl,--no-whole-archive" || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
./config zlib shared --prefix=/usr --openssldir=/etc/ssl --libdir=lib64
## make_prepend content
make depend LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a -Wl,--no-whole-archive -Wl,--no-whole-archive"
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a -Wl,--no-whole-archive -Wl,--no-whole-archive"

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
i386 ./config no-ssl zlib shared no-rc4 no-ssl2 no-ssl3 no-asm --prefix=/usr --openssldir=/etc/ssl --libdir=lib32
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1620030466
rm -rf %{buildroot}
## install_macro_32 start
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
export CFLAGS_ORIG="$CFLAGS"
export LDFLAGS_ORIG="$LDFLAGS"
export CXXFLAGS_ORIG="$CXXFLAGS"
export CFLAGS="$CFLAGS_ORIG -m32 -fno-lto -mstackrealign"
export LDFLAGS="$LDFLAGS_ORIG -m32 -fno-lto -mstackrealign"
export CXXFLAGS="$CXXFLAGS_ORIG -m32 -fno-lto -mstackrealign"
make DESTDIR=%{buildroot} MANDIR=/usr/share/man MANSUFFIX=openssl install V=1 VERBOSE=1
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
## install_macro_32 end
## install_macro start
unset PKG_CONFIG_PATH
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export CFLAGS="$CFLAGS_USE -m64 -flto=16"
export LDFLAGS="$LDFLAGS_USE -m64 -flto=16"
export CXXFLAGS="$CXXFLAGS_USE -m64 -flto=16"
make DESTDIR=%{buildroot} MANDIR=/usr/share/man MANSUFFIX=openssl install V=1 VERBOSE=1
## install_macro end
## Remove excluded files
rm -f %{buildroot}/usr/share/defaults/ssl/openssl.cnf
rm -f %{buildroot}/usr/bin/c_rehash
rm -f %{buildroot}/usr/bin/openssl
rm -f %{buildroot}/usr/include/openssl/aes.h
rm -f %{buildroot}/usr/include/openssl/asn1.h
rm -f %{buildroot}/usr/include/openssl/asn1_mac.h
rm -f %{buildroot}/usr/include/openssl/asn1t.h
rm -f %{buildroot}/usr/include/openssl/async.h
rm -f %{buildroot}/usr/include/openssl/bio.h
rm -f %{buildroot}/usr/include/openssl/blowfish.h
rm -f %{buildroot}/usr/include/openssl/bn.h
rm -f %{buildroot}/usr/include/openssl/buffer.h
rm -f %{buildroot}/usr/include/openssl/camellia.h
rm -f %{buildroot}/usr/include/openssl/cast.h
rm -f %{buildroot}/usr/include/openssl/cmac.h
rm -f %{buildroot}/usr/include/openssl/cms.h
rm -f %{buildroot}/usr/include/openssl/comp.h
rm -f %{buildroot}/usr/include/openssl/conf.h
rm -f %{buildroot}/usr/include/openssl/conf_api.h
rm -f %{buildroot}/usr/include/openssl/crypto.h
rm -f %{buildroot}/usr/include/openssl/ct.h
rm -f %{buildroot}/usr/include/openssl/des.h
rm -f %{buildroot}/usr/include/openssl/dh.h
rm -f %{buildroot}/usr/include/openssl/dsa.h
rm -f %{buildroot}/usr/include/openssl/dtls1.h
rm -f %{buildroot}/usr/include/openssl/e_os2.h
rm -f %{buildroot}/usr/include/openssl/ebcdic.h
rm -f %{buildroot}/usr/include/openssl/ec.h
rm -f %{buildroot}/usr/include/openssl/ecdh.h
rm -f %{buildroot}/usr/include/openssl/ecdsa.h
rm -f %{buildroot}/usr/include/openssl/engine.h
rm -f %{buildroot}/usr/include/openssl/err.h
rm -f %{buildroot}/usr/include/openssl/evp.h
rm -f %{buildroot}/usr/include/openssl/hmac.h
rm -f %{buildroot}/usr/include/openssl/idea.h
rm -f %{buildroot}/usr/include/openssl/kdf.h
rm -f %{buildroot}/usr/include/openssl/lhash.h
rm -f %{buildroot}/usr/include/openssl/md2.h
rm -f %{buildroot}/usr/include/openssl/md4.h
rm -f %{buildroot}/usr/include/openssl/md5.h
rm -f %{buildroot}/usr/include/openssl/mdc2.h
rm -f %{buildroot}/usr/include/openssl/modes.h
rm -f %{buildroot}/usr/include/openssl/obj_mac.h
rm -f %{buildroot}/usr/include/openssl/objects.h
rm -f %{buildroot}/usr/include/openssl/ocsp.h
rm -f %{buildroot}/usr/include/openssl/opensslconf.h
rm -f %{buildroot}/usr/include/openssl/opensslv.h
rm -f %{buildroot}/usr/include/openssl/ossl_typ.h
rm -f %{buildroot}/usr/include/openssl/pem.h
rm -f %{buildroot}/usr/include/openssl/pem2.h
rm -f %{buildroot}/usr/include/openssl/pkcs12.h
rm -f %{buildroot}/usr/include/openssl/pkcs7.h
rm -f %{buildroot}/usr/include/openssl/rand.h
rm -f %{buildroot}/usr/include/openssl/rc2.h
rm -f %{buildroot}/usr/include/openssl/rc4.h
rm -f %{buildroot}/usr/include/openssl/rc5.h
rm -f %{buildroot}/usr/include/openssl/ripemd.h
rm -f %{buildroot}/usr/include/openssl/rsa.h
rm -f %{buildroot}/usr/include/openssl/safestack.h
rm -f %{buildroot}/usr/include/openssl/seed.h
rm -f %{buildroot}/usr/include/openssl/sha.h
rm -f %{buildroot}/usr/include/openssl/srp.h
rm -f %{buildroot}/usr/include/openssl/srtp.h
rm -f %{buildroot}/usr/include/openssl/ssl.h
rm -f %{buildroot}/usr/include/openssl/ssl2.h
rm -f %{buildroot}/usr/include/openssl/ssl3.h
rm -f %{buildroot}/usr/include/openssl/stack.h
rm -f %{buildroot}/usr/include/openssl/symhacks.h
rm -f %{buildroot}/usr/include/openssl/tls1.h
rm -f %{buildroot}/usr/include/openssl/ts.h
rm -f %{buildroot}/usr/include/openssl/txt_db.h
rm -f %{buildroot}/usr/include/openssl/ui.h
rm -f %{buildroot}/usr/include/openssl/whrlpool.h
rm -f %{buildroot}/usr/include/openssl/x509.h
rm -f %{buildroot}/usr/include/openssl/x509_vfy.h
rm -f %{buildroot}/usr/include/openssl/x509v3.h
rm -f %{buildroot}/usr/lib32/engines-1.1/afalg.so
rm -f %{buildroot}/usr/lib32/engines-1.1/capi.so
rm -f %{buildroot}/usr/lib32/engines-1.1/padlock.so
rm -f %{buildroot}/usr/lib32/libcrypto.so
rm -f %{buildroot}/usr/lib32/libssl.so
rm -f %{buildroot}/usr/lib32/pkgconfig/32libcrypto.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libssl.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32openssl.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libcrypto.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libssl.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/openssl.pc
rm -f %{buildroot}/usr/lib64/engines-1.1/afalg.so
rm -f %{buildroot}/usr/lib64/engines-1.1/capi.so
rm -f %{buildroot}/usr/lib64/engines-1.1/padlock.so
rm -f %{buildroot}/usr/lib64/libcrypto.so
rm -f %{buildroot}/usr/lib64/libssl.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libcrypto.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libssl.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/openssl.pc
## install_append content
#install -D -m0644 apps/openssl.cnf %{buildroot}/usr/share/defaults/ssl/openssl.cnf
rm -rf %{buildroot}/etc/ssl
rm -rf %{buildroot}/usr/share/doc/openssl/html
rm -rf %{buildroot}/usr/share/man/
## install_append end

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcrypto.so.1.1
/usr/lib64/libssl.so.1.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcrypto.so.1.1
/usr/lib32/libssl.so.1.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcrypto.a
/usr/lib64/libssl.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libcrypto.a
/usr/lib32/libssl.a
