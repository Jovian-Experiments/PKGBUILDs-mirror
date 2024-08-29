# Maintainer: Ludovico de Nittis <ludovico.denittis@collabora.com>

pkgname=atomupd-daemon
pkgver=0.20240827.1
pkgrel=1
pkgdesc='Atomic updates daemon'
arch=('x86_64')
url='https://gitlab.steamos.cloud/holo/atomupd-daemon'
license=('MIT')
makedepends=('git' 'meson' 'python-dbusmock'
  'python>=3.11'
  'python<3.12'
)
depends=('dbus' 'glib2' 'json-glib' 'steamos-atomupd-client' 'polkit' 'systemd')
provides=("${pkgname}")
conflicts=("${pkgname}")
source=("${pkgname}::git+${url}.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
  arch-meson "${pkgname}" build
  meson compile -C build
}

check() {
  export DBUS_SESSION_BUS_ADDRESS=`dbus-daemon --fork --config-file=/usr/share/dbus-1/session.conf --print-address`
  # A new system bus is needed for the mock polkit
  export DBUS_SYSTEM_BUS_ADDRESS=`dbus-daemon --fork --config-file="${pkgname}"/ci/dbus_system.conf --print-address`

  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --destdir "$pkgdir"
  install -d -o root -g 102 -m 750 "${pkgdir}"/usr/share/polkit-1/rules.d
}

