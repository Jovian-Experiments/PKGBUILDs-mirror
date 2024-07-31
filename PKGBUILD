# Maintainer: Joshua Ashton <joshua@froggi.es>
# Contributor: AndyRTR <andyrtr@archlinux.org>

pkgname=xorg-xwayland
pkgver=24.1.1
pkgrel=1
arch=('x86_64')
license=(
    LicenseRef-Adobe-Display-PostScript
    BSD-3-Clause
    LicenseRef-DEC-3-Clause
    HPND
    LicenseRef-HPND-sell-MIT-disclaimer-xserver
    HPND-sell-variant
    ICU
    ISC
    MIT
    MIT-open-group
    NTP
    SGI-B-2.0
    SMLNJ
    X11
    X11-distribute-modifications-variant
)
groups=('xorg')
url="https://xorg.freedesktop.org"
pkgdesc="run X clients under wayland"
depends=('nettle' 'libepoxy' 'libxfont2' 'pixman'
         'xorg-server-common' 'libxcvt' 'mesa'
         'libglvnd' 'libxau' 'wayland' 'libdrm' 'libtirpc'
         'libei' 'libxshmfence' 'glibc')
makedepends=('meson' 'xorgproto' 'xtrans' 'libxkbfile' 'dbus'
             'xorg-font-util' 'wayland-protocols' 'mesa-libgl'
             'systemd')
source=(https://xorg.freedesktop.org/archive/individual/xserver/xwayland-$pkgver.tar.xz)
sha512sums=('e44f47adab3830846360fd05fdc06d9016832133c662f2e4b0763b98de0c9b48dbfce7d757ffea5538b5fabb68170e5d1057acc1b9a086e396b147deaa750998')
provides=('xorg-server-xwayland')
conflicts=('xorg-server-xwayland')
replaces=('xorg-server-xwayland')


build() {
  arch-meson xwayland-$pkgver build \
    -D ipv6=true \
    -D xvfb=false \
    -D xdmcp=false \
    -D xcsecurity=true \
    -D dri3=true \
    -D glamor=true \
    -D xkb_dir=/usr/share/X11/xkb \
    -D xkb_output_dir=/var/lib/xkb

  # Print config
  meson configure build
  ninja -C build
}

package() {

  DESTDIR="${pkgdir}" ninja -C build install
  # xorg-server-common file /usr/lib/xorg/protocol.txt
  rm "${pkgdir}"/usr/lib/xorg/protocol.txt
  rmdir "${pkgdir}"/usr/lib/xorg
  rm "${pkgdir}"/usr/share/man/man1/Xserver.1

  # license
  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" xwayland-$pkgver/COPYING
}
