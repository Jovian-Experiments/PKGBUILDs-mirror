# Maintainer: AndyRTR <andyrtr@archlinux.org>

# When releasing a xorgproto version with updated keysyms, rebuild libx11

pkgname=xorgproto
pkgver=2024.1
pkgrel=2
pkgdesc="combined X.Org X11 Protocol headers"
arch=('any')
url="https://xorg.freedesktop.org/"
license=(BSD-2-Clause
         HPND
         HPND-sell-variant
         ICU
         MIT
         MIT-open-group
         SGI-B-2.0
         SMLNJ
         X11
         X11-distribute-modifications-variant)
makedepends=('xorg-util-macros' 'meson')
checkdepends=('python-libevdev')
source=(https://xorg.freedesktop.org/archive/individual/proto/$pkgname-$pkgver.tar.xz)
sha512sums=('63955cb604ff831575af2193548857c1b99e52d00206ea9421ce99e145094bcd907388c4574bc32174a01cbe2c940b0377bf75ae7d2c0f953157dc9c32e5a07f')
#validpgpkeys=('3C2C43D9447D5938EF4551EBE23B7E70B467F0BF') # "Peter Hutterer (Who-T) <office@who-t.net>"
#validpgpkeys=('FD0004A26EADFE43A4C3F249C6F7AE200374452D') # "Povilas Kanapickas <povilas@radix.lt>"
validpgpkeys=('67DC86F2623FC5FD4BB5225D14706DBE1E4B4540') # "Olivier Fourdan <fourdan@xfce.org>"

prepare() {
  mkdir build
}

build() {
  arch-meson "$pkgname"-$pkgver build
  ninja -C build
}

check() {
  meson test -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install

  # missing docs
  install -m755 -d "${pkgdir}/usr/share/doc/${pkgname}"
  install -m644 "$pkgname"-$pkgver/PM_spec "${pkgdir}/usr/share/doc/${pkgname}/"

  # licenses
  install -m755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m644 "$pkgname"-$pkgver/COPYING* "${pkgdir}/usr/share/licenses/${pkgname}/"
  # remove licences of legacy stuff we don't ship anymore
  rm -f "${pkgdir}"/usr/share/licenses/${pkgname}/COPYING-{evieproto,fontcacheproto,lg3dproto,printproto,xcalibrateproto,xf86rushproto}

  # cleanup
  rm -f "${pkgdir}"/usr/include/X11/extensions/apple*
  rm -f "${pkgdir}"/usr/share/licenses/${pkgname}/COPYING-{apple,windows}wmproto
  rm -f "${pkgdir}"/usr/share/pkgconfig/applewmproto.pc
}
