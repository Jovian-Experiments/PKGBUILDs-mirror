# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinxu.org>
# Contributor: Wael Nasreddine <gandalf@siemens-mobiles.org>
# Contributor: Tor Krill <tor@krill.nu>
# Contributor: Will Rea <sillywilly@gmail.com>
# Contributor: Valentine Sinitsyn <e_val@inbox.ru>

pkgbase=networkmanager
pkgname=(
  networkmanager
  libnm
  nm-cloud-setup
)
pkgver=1.44.2
pkgrel=3.4
pkgdesc="Network connection manager and user applications"
url="https://networkmanager.dev/"
arch=(x86_64)
license=(GPL)
makedepends=(
  audit
  bluez-libs
  curl
  dhclient
  dhcpcd
  dnsmasq
  git
  glib2-docs
  gobject-introspection
  gtk-doc
  iproute2
  iptables
  iwd
  jansson
  libmm-glib
  libndp
  libnewt
  libpsl
  libteam
  meson
  modemmanager
  nftables
  nss
  openresolv
  pacrunner
  perl-yaml
  polkit
  ppp
  'python>=3.11'
  'python<3.12'
  python-gobject
  systemd
  vala
  vala
  wpa_supplicant
)
checkdepends=(
  libx11
  python-dbus
)
_commit=8bee6ef894a27ffc8a464df3b32b03e811e1a15d  # tags/1.44.2^0
source=(
  "git+https://gitlab.freedesktop.org/NetworkManager/NetworkManager.git#commit=$_commit"
  0001-connectivity-Make-curl-timeout-callback-non-repeatin.patch
  # https://gitlab.steamos.cloud/jupiter/tasks/-/issues/520
  # https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/1264
  "0002-iwd-remove-8021X-unknown-network-restrictions.patch")
b2sums=('SKIP'
        '51674577e4a2786b6491fdf90cc90734da3792e0a7e224f0eecc9c485a5f81b68a71bb559b23d294d52dc9065ee82c997c31f9272504c3d753e0ffe1321367e9'
        'acb84792effee07ff8853f85136d5fe2822f11810a82a6dbb071c9dba7051d9f5ad232e49442b78cf3b29f24caf9e947ee18941adbe3e1876c11f7212e055509')

pkgver() {
  cd NetworkManager
  git describe --tags | sed 's/-dev/dev/;s/-rc/rc/;s/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd NetworkManager

  patch -Np1 < ../0002-iwd-remove-8021X-unknown-network-restrictions.patch

  # https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/1756
  git apply -3 ../0001-connectivity-Make-curl-timeout-callback-non-repeatin.patch
}

build() {
  local meson_options=(
    # build checks this option; injecting just via *FLAGS is broken
    -D b_lto=true

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
    -D teamdctl=true
    -D bluez5_dun=true
    -D ebpf=true

    # configuration plugins
    -D config_plugins_default=keyfile
    -D ifupdown=false

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

  # NM uses malloc_usable_size in code copied from systemd
  CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"

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
  depends=(
    audit
    bluez-libs
    curl
    iproute2
    jansson
    libmm-glib
    libndp
    libnewt
    libnm
    libpsl
    libteam
    mobile-broadband-provider-info
    wpa_supplicant
  )
  optdepends=(
    'bluez: Bluetooth support'
    'dhclient: alternative DHCP client'
    'dhcpcd: alternative DHCP client'
    'dnsmasq: connection sharing'
    'firewalld: firewall support'
    'iptables: connection sharing'
    'iwd: wpa_supplicant alternative'
    'modemmanager: cellular network support'
    'nftables: connection sharing'
    'openresolv: alternative resolv.conf manager'
    'pacrunner: PAC proxy support'
    'polkit: let non-root users control networking'
    'ppp: dialup connection support'
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

  # Not actually packaged (https://bugs.archlinux.org/task/69138)
  _pick ovs usr/lib/systemd/system/NetworkManager.service.d/NetworkManager-ovs.conf

  # Restore empty dir
  install -d usr/lib/NetworkManager/dispatcher.d/no-wait.d
}

package_libnm() {
  pkgdesc="NetworkManager client library"
  license=(LGPL)
  depends=(
    glib2
    nss
    systemd-libs
    util-linux-libs
  )
  provides=(libnm.so)

  mv libnm/* "$pkgdir"
}

package_nm-cloud-setup() {
  pkgdesc="Automatically configure NetworkManager in cloud"
  depends=(networkmanager)

  mv cloud/* "$pkgdir"
}

# vim:set sw=2 sts=-1 et:
