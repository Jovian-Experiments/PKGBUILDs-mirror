# Author : Clayton Craft <clayton@igalia.com>

pkgname='steamos-systemreport'
pkgver=0.4
pkgrel=1
pkgdesc='System report collection tool'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(
  'steamos-systemreport'
  'steamos-systemreport-privileged'
  'org.valve.steamos.systemreport.policy'
)
sha256sums=(
  'e4a1560ab6d4bfdd4a66ad4cb778599c36e5328c74abe850d7032efc9da4f8b8'
  '83925eee8756d9fad8a6758d77bc386ac1d8733dd9836f66ff1b695bf36b2d39'
  'b36473e3b77307450e75c59e248dde34d95b69c6c765a425fc30d9e201e23067'
)

package() {
  depends=(
    'bash'
    'rauc'                           # rauc status
    'drm_info'                       # drm_info
    'upower'                         # upower
    'wireplumber'                    # wpctl
    'iputils'                        # ping
    'iproute2'                       # ip
    'iwd'                            # iwctl
    'pciutils'                       # lspci
    'usbutils'                       # lsusb
    'systemd'                        # coredumpctl, journalctl
    'procps-ng'                      # ps
    'util-linux'                     # lsblk, hexdump
    'parted'                         # parted
    'smartmontools'                  # smartctl
    'steamos-customizations-jupiter' # steamos-{readonly,dump-info}
    'jupiter-hw-support'             # amd_system_info
    'polkit'
  )
  install -Dm755 steamos-systemreport -t "$pkgdir"/usr/bin/
  install -Dm755 steamos-systemreport-privileged -t "$pkgdir"/usr/bin/steamos-polkit-helpers
  install -m755 -d "$pkgdir"/usr/share/polkit-1/actions
  install -m644 org.valve.steamos.systemreport.policy -t "$pkgdir"/usr/share/polkit-1/actions
}
