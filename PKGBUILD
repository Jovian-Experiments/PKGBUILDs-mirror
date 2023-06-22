# Maintainer: Jo Bates <jo@valvesoftware.com>

pkgname=upower
pkgver=0.99.15.jupiter
pkgrel=1.1
pkgdesc="Abstraction for enumerating power devices, listening to device events and querying history and statistics"
url="https://upower.freedesktop.org"
arch=(x86_64)
license=(GPL)
depends=(systemd libimobiledevice libgudev)
makedepends=(docbook-xsl gobject-introspection python git openssh gtk-doc meson)
checkdepends=(python-{dbus,dbusmock,gobject,packaging} umockdev)
backup=(etc/UPower/UPower.conf)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/upower.git#commit=v$pkgver")
sha256sums=('SKIP')

pkgver() {
  cd upower
  git describe --tags | sed -e 's/^v\|^UPOWER_//;s/_/\./g;s/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd upower
}

build() {
  arch-meson upower build
  meson compile -C build
}

# Holo: self-tests fail on python 3.11.  Can come back after next rebase.
#
# check() {
#   meson test -C build --print-errorlogs
# }

package() {
  depends+=(libg{lib,object,io}-2.0.so)
  provides+=(libupower-glib.so)

  meson install -C build --destdir "$pkgdir"
}
