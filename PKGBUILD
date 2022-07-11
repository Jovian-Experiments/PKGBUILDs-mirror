# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinxu.org>
# Contributor: Wael Nasreddine <gandalf@siemens-mobiles.org>
# Contributor: Tor Krill <tor@krill.nu>
# Contributor: Will Rea <sillywilly@gmail.com>
# Contributor: Valentine Sinitsyn <e_val@inbox.ru>

pkgbase=networkmanager
pkgname=(networkmanager libnm nm-cloud-setup)
pkgver=1.34.0
pkgrel=1.1
pkgdesc="Network connection manager and user applications"
url="https://networkmanager.dev/"
arch=(x86_64)
license=(GPL)
_pppver=2.4.9
# XXX: Change the iptables-nft -> iptables makedep.
# See: https://bugs.archlinux.org/task/75101
makedepends=(intltool dhclient dhcpcd iptables gobject-introspection gtk-doc
             "ppp=$_pppver" modemmanager iproute2 nss polkit wpa_supplicant curl
             systemd libmm-glib libnewt libndp libteam nftables vala perl-yaml
             python-gobject git vala jansson bluez-libs glib2-docs iwd dnsmasq
             openresolv libpsl audit meson)
checkdepends=(libx11 python-dbus)
_commit=9133a30c9deb3a003a20b09a617a25b07ada18ae  # tags/1.34.0^0
source=("git+https://gitlab.freedesktop.org/NetworkManager/NetworkManager.git#commit=$_commit"
        # https://gitlab.steamos.cloud/jupiter/tasks/-/issues/520
        # https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/1264
        "0001-iwd-remove-8021X-unknown-network-restrictions.patch")
b2sums=('SKIP'
        '70edbe50dec9e2cd097478eed154680a56d0286ef34db03382e1b8747c2a8ba8e86e16cee1c77d983bf9b32495d9b4b2b04b9898d1851497572b9176f0910f47')

pkgver() {
  cd NetworkManager
  git describe --tags | sed 's/-dev/dev/;s/-rc/rc/;s/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd NetworkManager

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done
}

build() {
  local meson_options=(
    # system paths
    -D dbus_conf_dir=/usr/share/dbus-1/system.d

    # platform
    -D dist_version="$pkgver-$pkgrel"
    -D session_tracking_consolekit=false
    -D suspend_resume=systemd
    -D modify_system=true
    -D selinux=false

    # features
    -D iwd=true
    -D pppd_plugin_dir=/usr/lib/pppd/$_pppver
    -D teamdctl=true
    -D nm_cloud_setup=true
    -D bluez5_dun=true
    -D ebpf=true

    # configuration plugins
    -D config_plugins_default=keyfile

    # handlers for resolv.conf
    -D netconfig=no
    -D config_dns_rc_manager_default=symlink

    # miscellaneous
    -D vapi=true
    -D docs=true
    -D more_asserts=no
    -D more_logging=false
    -D qt=false
  )

  arch-meson NetworkManager build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

package_networkmanager() {
  depends=(libnm iproute2 wpa_supplicant libmm-glib libnewt libndp libteam curl
           bluez-libs libpsl audit mobile-broadband-provider-info)
  optdepends=(
    'polkit: let non-root users control networking'
    'dnsmasq: connection sharing'
    'nftables: connection sharing'
    'iptables: connection sharing'
    'bluez: Bluetooth support'
    'ppp: dialup connection support'
    'modemmanager: cellular network support'
    'iwd: wpa_supplicant alternative'
    'dhclient: alternative DHCP client'
    'dhcpcd: alternative DHCP client'
    'openresolv: alternative resolv.conf manager'
    'firewalld: firewall support'
  )
  backup=(etc/NetworkManager/NetworkManager.conf)

  meson install -C build --destdir "$pkgdir"

  cd "$pkgdir"

  # /etc/NetworkManager
  install -d etc/NetworkManager/{conf,dnsmasq}.d
  install -dm700 etc/NetworkManager/system-connections
  install -m644 /dev/stdin etc/NetworkManager/NetworkManager.conf <<END
# Configuration file for NetworkManager.
# See "man 5 NetworkManager.conf" for details.
END

  # packaged configuration
  install -Dm644 /dev/stdin usr/lib/NetworkManager/conf.d/20-connectivity.conf <<END
[connectivity]
uri=http://ping.archlinux.org/nm-check.txt
END

  shopt -s globstar

  _pick libnm usr/include/libnm
  _pick libnm usr/lib/girepository-1.0/NM-*
  _pick libnm usr/lib/libnm.*
  _pick libnm usr/lib/pkgconfig/libnm.pc
  _pick libnm usr/share/gir-1.0/NM-*
  _pick libnm usr/share/gtk-doc/html/libnm
  _pick libnm usr/share/vala/vapi/libnm.*

  _pick cloud usr/lib/**/*nm-cloud-setup*
  _pick cloud usr/share/man/*/nm-cloud-setup*

  # Restore empty dir
  install -d usr/lib/NetworkManager/dispatcher.d/no-wait.d
}

package_libnm() {
  pkgdesc="NetworkManager client library"
  license=(LGPL)
  depends=(glib2 nss util-linux-libs jansson systemd-libs)
  provides=(libnm.so)

  mv libnm/* "$pkgdir"
}

package_nm-cloud-setup() {
  pkgdesc="Automatically configure NetworkManager in cloud"
  depends=(networkmanager)

  mv cloud/* "$pkgdir"
}

# vim:set sw=2 et:
