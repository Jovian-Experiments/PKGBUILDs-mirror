# Maintainer: Dave Reisner <dreisner@archlinux.org>

pkgname=kmod
pkgver=30
# SteamOS use /usr/lib/steamos/modules
pkgrel=1.4
pkgdesc="Linux kernel module management tools and library"
arch=('x86_64')
url='https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git'
license=('GPL2')
depends=('glibc' 'zlib' 'openssl' 'xz' 'zstd')
checkdepends=('linux-headers' 'libelf')
options=('strip' 'debug')
provides=('module-init-tools=3.16' 'libkmod.so')
conflicts=('module-init-tools')
replaces=('module-init-tools')
validpgpkeys=('EAB33C9690013C733916AC839BA2A5A630CBEA53')  # Lucas DeMarchi
source=("https://www.kernel.org/pub/linux/utils/kernel/$pkgname/$pkgname-$pkgver.tar."{xz,sign}
        '0001-master.patch'
        'depmod-search.conf'
        'depmod.hook'
        'depmod.script')
md5sums=('85202f0740a75eb52f2163c776f9b564'
         'SKIP'
         '109042785e725717fe6a6d545c51a090'
         'dd62cbf62bd8f212f51ef8c43bec9a77'
         'dbc0f24bb7d5a63f38b4a42a7499cdaf'
         'b00253ca0d4ebfb2414e4596597bdebd')
sha256sums=('f897dd72698dc6ac1ef03255cd0a5734ad932318e4adbaebc7338ef2f5202f9f'
            'SKIP'
            '99a02347c809307675a9a643ec34704ec5289b754d53dd4d319b32849b299c60'
            '1a92bfeae870f61ce814577e69d2a147a9c0caf6aed1131243e4179241fcc4a8'
            '4c96f1fda1b4893d03e0ce2c377442bb39e30cd76a85103ede4e93b7d1d5701d'
            'd2cd04a09feba30e1376144a8110ec7521892acb0940c3c4ba459aeecf0452ed')

prepare() {
  cd "$pkgname-$pkgver"

  patch -Np1 < ../0001-master.patch
}

build() {
  cd "$pkgname-$pkgver"

  ./configure \
    --sysconfdir=/etc \
    --with-xz \
    --with-zlib \
    --with-zstd \
    --with-openssl

  make
}

check() {
  # As of kmod v20, the test suite needs to build some kernel modules, and thus
  # needs headers available in order to run. We depend on linux-headers, but
  # this is really only to try and make sure that *some* useable tree of kernel
  # headers exist. The first useable tree we find is good enough, as these
  # modules will never be loaded by tests.

  # SteamOS: Also check /usr/lib/steamos/modules/ used by the vanilla linux packages for module indirection.
  local kdirs=(/usr/lib/{/steamos,}/modules/*/build/Makefile)
  if [[ ! -f ${kdirs[0]} ]]; then
    printf '==> Unable to find kernel headers to build modules for tests\n' >&2
    return 1
  fi

  local kver kdir=${kdirs[0]%/Makefile}
  IFS=/ read _ _ _ kver _ <<<"$kdir"

  make -C "$pkgname-$pkgver" check KDIR="$kdir" KVER="$kver"
}

package() {
  make -C "$pkgname-$pkgver" DESTDIR="$pkgdir" install

  # extra directories
  install -dm755 "$pkgdir"/{etc,usr/lib}/{depmod,modprobe}.d

  for tool in {ins,ls,rm,dep}mod mod{probe,info}; do
    ln -s kmod "$pkgdir/usr/bin/$tool"
  done

  # install depmod.d file for search/ dir
  install -Dm644 "$srcdir/depmod-search.conf" "$pkgdir/usr/lib/depmod.d/search.conf"

  # hook
  install -Dm644 "$srcdir/depmod.hook" "$pkgdir/usr/share/libalpm/hooks/60-depmod.hook"
  install -Dm755 "$srcdir/depmod.script" "$pkgdir/usr/share/libalpm/scripts/depmod"
}

# vim: ft=sh syn=sh et
