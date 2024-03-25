# Maintainer: Jeremy Whiting <jeremy.whiting@collabora.com>

pkgname=steamos-manager
_srctag=v0.20240208.0
pkgver=${_srctag//-/./}
pkgrel=2
pkgdesc='SteamOS Manager daemon - Exposses steamos scripts via dbus for steam client to use.'
arch=('x86_64')
url='https://store.steampowered.com/steamos/'
license=('LGPL2.1')
depends=(gcc-libs glibc)
makedepends=(git cargo)
provides=("$pkgname")
conflicts=("$pkgname")
source=("$pkgname::git+https://gitlab.steamos.cloud/holo/$pkgname.git#tag=${_srctag}")
md5sums=('SKIP')

prepare() {
	export RUSTUP_TOOLCHAIN=stable
	cd "$pkgname"
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	cd "$pkgname"
	cargo build -r
}

package () {
	cd "$pkgname"
	install -d -m0755 "$pkgdir/usr/share/dbus-1/system-services/"
	install -d -m0755 "$pkgdir/usr/share/dbus-1/system.d/"
	install -d -m0755 "$pkgdir/usr/lib/systemd/system/"
	install -Dm755 "target/release/steamos-manager" "$pkgdir/usr/lib/steamos-manager"
	install -Dm644 "data/com.steampowered.SteamOSManager1.service" "$pkgdir/usr/share/dbus-1/system-services/"
	install -Dm644 "data/com.steampowered.SteamOSManager1.conf" "$pkgdir/usr/share/dbus-1/system.d/"
	install -Dm644 "data/steamosmanager.service" "$pkgdir/usr/lib/systemd/system/"
  install -Dm755 "bin/steamos-enable-wifidebug" "$pkgdir/usr/lib/"
  install -Dm755 "bin/steamos-disable-wifidebug" "$pkgdir/usr/lib"
  install -Dm755 "bin/steamos-get-wifidebug" "$pkgdir/usr/lib"
}
