# Maintainer: Ludovico de Nittis <ludovico.denittis@collabora.com>

pkgname=atomupd-daemon-git
pkgver=0.20220323.0.r0.g36d2fcb
pkgrel=2
_tag=v0.20220323.0
pkgdesc='Atomic updates daemon'
arch=('x86_64')
url='https://gitlab.steamos.cloud/steam/atomupd-daemon'
license=('MIT')
makedepends=('git' 'meson')
depends=('dbus' 'glib2' 'json-glib' 'steamos-atomupd-client-git>=r157.4d50d6d' 'systemd')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+${url}.git#tag=$_tag")
sha256sums=('SKIP')

pkgver() {
  cd "${pkgname%-git}"
  # cutting off 'v' prefix that presents in the git tag
  git describe --long | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  arch-meson "${pkgname%-git}" build
  meson compile -C build
}

check() {
  export DBUS_SESSION_BUS_ADDRESS=`dbus-daemon --fork --config-file=/usr/share/dbus-1/session.conf --print-address`
  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --destdir "$pkgdir"
}

