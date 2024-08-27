# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Robin Candau <antiz@archlinux.org>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>

pkgbase=bluez
#pkgname=('bluez' 'bluez-utils' 'bluez-libs' 'bluez-cups' 'bluez-hid2hci' 'bluez-plugins')
# Jupiter: ship only a avdtptest package
pkgname=('bluez-avdtptest')
pkgver=5.71
pkgrel=2.2 # See Jupiter sections
url="http://www.bluez.org/"
arch=('x86_64')
license=('GPL2')
makedepends=('dbus' 'libical' 'systemd' 'alsa-lib' 'json-c' 'ell' 'python-docutils' 'python>=3.11' 'python<3.12')
# Jupiter: required for other Android tools
makedepends+=('sbc' 'speexdsp')
pkgdesc="The Android avdtptest tool"
source=(https://www.kernel.org/pub/linux/bluetooth/${pkgbase}-${pkgver}.tar.{xz,sign}
        bluetooth.modprobe
        fix-bluez-5.71-autoconnection.diff)
# see https://www.kernel.org/pub/linux/bluetooth/sha256sums.asc
sha256sums=('b828d418c93ced1f55b616fb5482cf01537440bfb34fbda1a564f3ece94735d8'
            'SKIP'
            '46c021be659c9a1c4e55afd04df0c059af1f3d98a96338236412e449bf7477b4'
            '7b19092fa09f8b04314cda3e9d14e69ef79bd85bc4f19ca2e15c35ebbb486e48')
validpgpkeys=('E932D120BC2AEC444E558F0106CA9F5D1DCF2659') # Marcel Holtmann <marcel@holtmann.org>

prepare() {
  cd "${pkgbase}"-${pkgver}
  # fix autoconnection - https://github.com/bluez/bluez/issues/686
  # https://github.com/tedd-an/bluez-upstream-test/pull/484
  patch -Np1 -i ../fix-bluez-5.71-autoconnection.diff
}

build() {
  cd "${pkgbase}"-${pkgver}
  # Jupiter: enable android for avdtptest, disable the rest
  ./configure \
          --prefix=/usr \
          --mandir=/usr/share/man \
          --sysconfdir=/etc \
          --localstatedir=/var \
          --libexecdir=/usr/lib \
          --with-dbusconfdir=/usr/share \
          --enable-android \
          --disable-btpclient \
          --disable-midi \
          --disable-sixaxis \
          --disable-mesh \
          --disable-hid2hci \
          --disable-experimental \
          --disable-library # this is deprecated
  make
}

check() {
  # Jupiter: no tests needed
  return 0
  cd "$pkgbase"-$pkgver
  # fails test-vcp - https://github.com/bluez/bluez/issues/683
  make check || /bin/true
}

# Jupiter: minimal package/target
package() {
  depends=('glib2' 'glibc')

  # There's no make install target
  install -Dm755 "$srcdir/$pkgbase-$pkgver/android/avdtptest" "$pkgdir/usr/bin/avdtptest"
}

package_bluez() {
  pkgdesc="Daemons for the bluetooth protocol stack"
  depends=('libical' 'dbus' 'glib2' 'alsa-lib' 'json-c' 'glibc')
  backup=('etc/bluetooth/main.conf')
  conflicts=('obexd-client' 'obexd-server')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR=${pkgdir} \
       install-pkglibexecPROGRAMS \
       install-dbussessionbusDATA \
       install-systemdsystemunitDATA \
       install-systemduserunitDATA \
       install-dbussystembusDATA \
       install-dbusDATA \
       install-man8

  # ship upstream main config file
  install -dm555 "${pkgdir}"/etc/bluetooth
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/src/main.conf "${pkgdir}"/etc/bluetooth/main.conf

  # add basic documention
  install -dm755 "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis
  cp -a doc/*.txt "${pkgdir}"/usr/share/doc/"${pkgbase}"/dbus-apis/
  # fix module loading errors
  install -dm755 "${pkgdir}"/usr/lib/modprobe.d
  install -Dm644 "${srcdir}"/bluetooth.modprobe "${pkgdir}"/usr/lib/modprobe.d/bluetooth-usb.conf
  # load module at system start required by some functions
  # https://bugzilla.kernel.org/show_bug.cgi?id=196621
  install -dm755 "$pkgdir"/usr/lib/modules-load.d
  echo "crypto_user" > "$pkgdir"/usr/lib/modules-load.d/bluez.conf

  # fix obex file transfer - https://bugs.archlinux.org/task/45816
  ln -fs /usr/lib/systemd/user/obex.service "${pkgdir}"/usr/lib/systemd/user/dbus-org.bluez.obex.service

  # FS#74157 - bluez systemd service fails without localstatedir present
  install -dm700 "${pkgdir}"/var/lib/bluetooth

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}

package_bluez-utils() {
  pkgdesc="Development and debugging utilities for the bluetooth protocol stack"
  depends=('dbus' 'systemd' 'systemd-libs' 'glib2' 'glibc' 'readline')
  optdepends=('ell: for btpclient'
              'json-c: for mesh-cfgclient')
  backup=('etc/bluetooth/mesh-main.conf')
  conflicts=('bluez-hcidump')
  provides=('bluez-hcidump')
  replaces=('bluez-hcidump' 'bluez<=4.101')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-binPROGRAMS \
       install-dist_zshcompletionDATA \
       install-man1

  # add missing tools FS#41132, FS#41687, FS#42716
  for files in `find tools/ -type f -perm -755`; do
    filename=$(basename $files)
    install -Dm755 "${srcdir}"/"${pkgbase}"-${pkgver}/tools/$filename "${pkgdir}"/usr/bin/$filename
  done

  # ship upstream mesh config file
  install -dm555 "${pkgdir}"/etc/bluetooth
  install -Dm644 "${srcdir}"/"${pkgbase}"-${pkgver}/mesh/mesh-main.conf "${pkgdir}"/etc/bluetooth/mesh-main.conf

  # libbluetooth.so* are part of libLTLIBRARIES and binPROGRAMS targets
  #make DESTDIR=${pkgdir} uninstall-libLTLIBRARIES
  #rmdir ${pkgdir}/usr/lib
  rm -rf "${pkgdir}"/usr/lib

  # move the hid2hci man page out
  mv "${pkgdir}"/usr/share/man/man1/hid2hci.1 "${srcdir}"/
}

package_bluez-libs() {
  pkgdesc="Deprecated libraries for the bluetooth protocol stack"
  depends=('glibc')
  provides=('libbluetooth.so')
  license=('LGPL2.1')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-pkgincludeHEADERS \
       install-libLTLIBRARIES \
       install-pkgconfigDATA
}

package_bluez-cups() {
  pkgdesc="CUPS printer backend for Bluetooth printers"
  depends=('cups' 'glib2' 'glibc' 'dbus')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" install-cupsPROGRAMS

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}

package_bluez-hid2hci() {
  pkgdesc="Put HID proxying bluetooth HCI's into HCI mode"
  depends=('systemd' 'systemd-libs' 'glibc')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR=${pkgdir} \
       install-udevPROGRAMS \
       install-rulesDATA

  install -dm755 "${pkgdir}"/usr/share/man/man1
  mv "${srcdir}"/hid2hci.1 "${pkgdir}"/usr/share/man/man1/hid2hci.1

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}

package_bluez-plugins() {
  pkgdesc="bluez plugins (PS3 Sixaxis controller)"
  depends=('systemd' 'systemd-libs' 'glibc')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-pluginLTLIBRARIES

  # cleanup  - these libs go into bluez-libs
  rm "${pkgdir}"/usr/lib/libbluetooth.so*
}
