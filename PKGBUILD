# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Maintainer (Holo): Alberto Garcia <berto@igalia.com>
# Contributor: Ionut Biru <ibiru@archlinux.org>

pkgname=udisks2
pkgver=2.9.4
pkgrel=1.2
pkgdesc="Disk Management Service, version 2"
arch=('x86_64')
url="https://www.freedesktop.org/wiki/Software/udisks"
license=('GPL2')
depends=('polkit' 'libatasmart' 'libgudev' 'libblockdev')
makedepends=('docbook-xsl' 'gobject-introspection' 'parted' 'gtk-doc')
optdepends=('gptfdisk: GUID partition table support'
            'ntfs-3g: NTFS filesystem management support'
            'dosfstools: VFAT filesystem management support')
backup=('etc/udisks2/udisks2.conf')
source=("https://github.com/storaged-project/udisks/archive/udisks-$pkgver.tar.gz"
        # Holo: Don't free static resources - https://github.com/storaged-project/udisks/pull/926
        "dont-free-static-resources.patch"
        # Holo: Sanitize the label when creating the mount point - https://github.com/storaged-project/udisks/issues/1056
        "sanitize-mount-point.patch"
        # Holo: Allow mounting a filesystem on behalf of another user - https://github.com/storaged-project/udisks/issues/1065
        "mount-other-user.patch")
sha512sums=('5b266cbc29f55d4c4a5100147793becf32a95f94bc7e184796bd2505a4e958a6bce9e5ffa584e4a89c7b874ed14ba6d9d096659565d0f51d860ef216d0cbd435'
            'a14cd7c6c52d585b145e96a8b111bd173a06c3bb58dc55db5e099677f24464f23caede27c260ddebcad07a6a9b0872878054a749346c2142e6dd3bdb240c9202'
            '4e9747fcf2fe81a7662fc827547d5ea9a46897061a40f4006b49736a86a1ded78aa6d51408ccb421d8a74258685d159efd555fe59e61c24f644650f5e04d469f'
            '0e3059748b7e8c2b9ded205f67bf1f661eca8e2e102756e61e9db7a63c03bd069c2cdc931dfab9da0d8221e440def2509e947a4c5a59f7188ef0509549bf4ef0')


prepare() {
  cd udisks-udisks-$pkgver

  # Remove these patches when UDisks 3.x is available
  patch -p1 < "$srcdir/dont-free-static-resources.patch"
  patch -p1 < "$srcdir/sanitize-mount-point.patch"
  patch -p1 < "$srcdir/mount-other-user.patch"

  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd udisks-udisks-$pkgver
  ./configure --prefix=/usr --sysconfdir=/etc \
      --sbindir=/usr/bin --libexecdir=/usr/lib \
      --with-systemdsystemunitdir=/usr/lib/systemd/system \
      --localstatedir=/var --disable-static \
      --enable-gtk-doc enable_available_modules=yes
  make
}

check() {
  cd udisks-udisks-$pkgver
  make check
}

package() {
  cd udisks-udisks-$pkgver
  make DESTDIR="$pkgdir" install
}
