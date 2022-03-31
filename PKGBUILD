# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>

pkgbase=bluez
pkgname=('bluez' 'bluez-utils' 'bluez-libs' 'bluez-cups' 'bluez-hid2hci' 'bluez-plugins')
pkgver=5.63
pkgrel=1.7
url="http://www.bluez.org/"
arch=('x86_64')
license=('GPL2')
makedepends=('dbus' 'libical' 'systemd' 'alsa-lib' 'json-c' 'ell' 'python-docutils')
source=(https://www.kernel.org/pub/linux/bluetooth/${pkgname}-${pkgver}.tar.{xz,sign}
        bluetooth.modprobe
	AVRCP_TG_MDI_BV-04-C.patch
	0001-adapter-Fix-crash-when-storing-link-key.patch
	0002-a2dp-Don-t-initialize-a2dp_sep-destroy-until-properl.patch
	0003-a2dp-Always-invalidate-the-cache-if-its-configuratio.patch
	0004-a2dp-Fix-crash-when-SEP-codec-has-not-been-initializ.patch
)
# see https://www.kernel.org/pub/linux/bluetooth/sha256sums.asc
sha256sums=('9349e11e8160bb3d720835d271250d8a7424d3690f5289e6db6fe07cc66c6d76'
            'SKIP'
            '46c021be659c9a1c4e55afd04df0c059af1f3d98a96338236412e449bf7477b4'
            'd64d7518a571251fc8cdb945a8f22aa4ef9f65864a46491034f561a1e5c54e37'
	    'fd73c3c80971a33d5ce8856c42e0abedfd5acd22da70a067a7a945ce475e1b7b'
	    'd5139c0359b8afd7db3471372f4f771ab12adc2c04ddc41d050284d27df5ea56'
	    '8d61267d77733997d20bafa1dd9fb7bc1f72fadaffa198aaebe287b6de96cd1a'
	    'c88f065634e314074e0af68ddb49cd7b8a6adc211ed5fd8d093181d1a2c64e4e')
validpgpkeys=('E932D120BC2AEC444E558F0106CA9F5D1DCF2659') # Marcel Holtmann <marcel@holtmann.org>

build() {
  cd "${pkgname}"-${pkgver}
  ./configure \
          --prefix=/usr \
          --mandir=/usr/share/man \
          --sysconfdir=/etc \
          --localstatedir=/var \
          --libexecdir=/usr/lib \
          --with-dbusconfdir=/usr/share \
          --disable-obex \
          --enable-btpclient \
          --enable-midi \
          --enable-sixaxis \
          --enable-mesh \
          --enable-hid2hci \
          --enable-experimental \
          --enable-library # this is deprecated
  make
}

check() {
  cd "$pkgname"-$pkgver
  # tests segfault and hang
#  make check || /bin/true # https://bugzilla.kernel.org/show_bug.cgi?id=196621
}

prepare() {
  patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/AVRCP_TG_MDI_BV-04-C.patch
  patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/0001-adapter-Fix-crash-when-storing-link-key.patch
  patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/0002-a2dp-Don-t-initialize-a2dp_sep-destroy-until-properl.patch
  patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/0003-a2dp-Always-invalidate-the-cache-if-its-configuratio.patch
  patch -d "${pkgname}"-${pkgver} -p1 -i "${srcdir}"/0004-a2dp-Fix-crash-when-SEP-codec-has-not-been-initializ.patch
}

package_bluez() {
  pkgdesc="Daemons for the bluetooth protocol stack"
  depends=('libical' 'dbus' 'glib2' 'alsa-lib' 'json-c')
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
  install -dm755 "${pkgdir}"/etc/bluetooth
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
}

package_bluez-utils() {
  pkgdesc="Development and debugging utilities for the bluetooth protocol stack"
  depends=('dbus' 'systemd' 'glib2')
  optdepends=('ell: for btpclient')
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
  depends=('cups')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" install-cupsPROGRAMS
}

package_bluez-hid2hci() {
  pkgdesc="Put HID proxying bluetooth HCI's into HCI mode"
  depends=('systemd')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR=${pkgdir} \
       install-udevPROGRAMS \
       install-rulesDATA
  
  install -dm755 "${pkgdir}"/usr/share/man/man1
  mv "${srcdir}"/hid2hci.1 "${pkgdir}"/usr/share/man/man1/hid2hci.1
}

package_bluez-plugins() {
  pkgdesc="bluez plugins (PS3 Sixaxis controller)"
  depends=('systemd')

  cd "${pkgbase}"-${pkgver}
  make DESTDIR="${pkgdir}" \
       install-pluginLTLIBRARIES
}
