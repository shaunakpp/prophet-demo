require 'csv'

CSV.open('imp.csv', 'wb') do |csv|
  csv << ['ds', 'y']
  CSV.foreach("account_report.csv") do |c|
    csv << [c[0], c[2]]
  end
end
